import os
import subprocess as sp
import multiprocessing as mp

# scavenger imports
import libpy

EXIT_MSG="""\
You may now exit out of this shell with the keys "ctrl+d" or the "exit" command'
"""

class Task:
    def main(self, argv):
        arg = argv[1]
        if arg == "setup":
            self.setup()
        elif arg == "run":
            self.run()
        elif arg == "cleanup":
            self.cleanup()

    def setup(self):
        """
        This is for setting up the environment for the task
        """
        exit(1)

    def run(self):
        """
        This runs a submission checker in the background and a shell for the
        user to work with in the foreground
        """
        exit(1)

    def run_checker(self):
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
        exit(1)

    def cleanup(self):
        """
        This is called whenever something goes wrong at any other point in
        the task.
        """
        exit(1)
