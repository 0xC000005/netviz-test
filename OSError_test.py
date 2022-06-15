import os
checkpointDir = "testFolder"

if __name__ == '__main__':
    # try:
    #     if os.path.exists(checkpointDir):
    #         print("Checkpoint directory already exist")
    #     else:
    #         os.mkdir(checkpointDir)
    #         print("Successfully created the directory %s " % checkpointDir)
    # except OSError:
    #     print("Creation of the directory %s failed" % checkpointDir)
    if os.path.exists(checkpointDir):
        print("Checkpoint directory already exist")
    else:
        os.mkdir(checkpointDir)
        print("Successfully created the directory %s " % checkpointDir)