import os
import subprocess as sp
import multiprocessing as mp
import traceback

# scavenger imports
import libpy

EXIT_MSG="""\
You may now exit out of this shell with the keys "ctrl+d" or the "exit" command'
"""

class Task:
    def main(self):
        try:
            self.setup()
            self.run()
        except Exception:
            print(traceback.format_exc())
            print("Calling cleanup()...")
            self.cleanup()
            exit(1)
        self.cleanup()

    def setup(self):
        """
        This is for setting up the environment for the task. Do stuff like
        creating directories, modifying files, etc.
        """
        raise libpy.UnimplementedError()

    def run(self):
        """
        This is for running the task that the user must complete.

        You can use this time to set the enviornment variables to manipulate
        the shell the user will be running.
        """
        raise libpy.UnimplementedError()

    def run_task(self):
        """
        Runs the checker in the background and a shell for the user in
        the foreground.
        """
        # Run the checker in the background
        checker_proc = mp.Process(target=self.checker)
        checker_proc.start()
        # Start a shell for the user to play with
        shell = sp.Popen(os.environ['SHELL'])
        shell.wait()
        # Clean up the checker once the user is done
        checker_proc.terminate()

    def checker(self):
        while True:
            with open(libpy.SUBMIT_PIPE) as fifo:
                if self.check_submission(fifo.read().strip()):
                    break

    def check_submission(self, submission):
        """
        This function will be called with every new submission.

        Return False to continue the loop, and True to exit out of it.
        """
        raise libpy.UnimplementedError()

    def cleanup(self):
        """
        This is called whenever something goes wrong at any other point in
        the task and once at the very end.
        """
        raise libpy.UnimplementedError()
