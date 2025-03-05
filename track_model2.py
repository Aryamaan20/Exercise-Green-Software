from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()

import os
os.system("poetry run baler --project CMS_workspace CMS_project_v1 --mode train")

tracker.stop()
