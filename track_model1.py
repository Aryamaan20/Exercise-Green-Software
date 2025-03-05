from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()

import os
os.system("poetry run baler --project CFD_workspace CFD_project_animation --mode train")

tracker.stop()
