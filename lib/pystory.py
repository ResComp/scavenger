import sys
import os
import traceback
import subprocess as sp

# scavenger imports
import libpy
import pystory

class Story:
    def __init__(self, tasks):
        """
        A list of task names
        """
        self.tasks = tasks

    def main(self):
        try:
            self.setup()
            self.run()
        except Exception:
            print(traceback.format_exc())
            print("Story error: Calling cleanup()...")
            self.cleanup()
        else:
            self.cleanup()

    def run_tasks(self, tasks):
        for task in tasks:
            question = "Would you like to continue with task {0}? ".format(task)
            if not self.get_consent(question):
                continue
            res_task = self.resolve_task(task)
            if res_task is None:
                continue
            taskname = os.path.basename(res_task)
            if self.run_single_task(res_task, taskname):
                continue
            err_msg = "ERROR: task {0} aborted".format(taskname)
            libpy.announce(err_msg, style=libpy.BOLD+libpy.RED)

    def get_consent(self, prompt):
        valid_resp = ["yes", "no"]
        resp = ''
        while resp not in valid_resp:
            if sys.version_info < (3,):
                resp = raw_input(prompt)
            else:
                resp = input(prompt)
            if resp not in valid_resp:
                reject = "Please respond yes or no"
                print(libpy.text(reject, style=libpy.BOLD+libpy.RED))
        if resp == "yes":
            return True
        return False

    def resolve_task(self, task):
        """
        Return None if no valid task is found
        Returns the absolute path of the task
        """
        if self.valid_task(task):
            return task
        taskpath = os.environ["SCAVENGERTASKPATH"].split(":")
        for path in taskpath:
            res_task = os.path.join(path, task)
            if self.valid_task(res_task):
                return res_task
        return None

    def valid_task(self, task):
        """
        Takes in an absolute path
        """
        return os.path.isfile(task) and os.access(task, os.X_OK)

    def run_single_task(self, task, taskname):
        """
        Takes in an absolute path to an executable

        Returns True if the task has an exit code of 0. Return False otherwise
        """
        env = os.environ.copy()
        env["HuntingPrompt"] = "{{{0}}}".format(taskname)
        child = sp.Popen(task, env=env)
        child.communicate()
        return child.returncode == 0

    def setup(self):
        raise libpy.UnimplementedError()

    def run(self):
        raise libpy.UnimplementedError()

    def cleanup(self):
        raise libpy.UnimplementedError()
