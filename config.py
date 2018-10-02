class SharedCfg:
    # Warning, DEBUG can be destructive as each it may delete the output files
    DEBUG_MODE = False

    # String: The name to give the output folder
    OUTPUT_FOLDER_NAME = "ModularNetworkMonitor-Output"


class MonitorCfg:
    # List of Strings: The modules to load/run
    MODULES = ["status/ping"]

    # Integer: How many times to check the network (0 for unlimited)
    LOOP_TIMES = 0

    # Integer: The time (in seconds) to wait after checking the network before checking it again
    LOOP_WAIT = 0


class PingCfg:
    # List of Strings: The hosts/IPs to ping
    PING_TARGETS = ["localhost", "1.1.1.1"]

    # Integer: How many times to ping each host
    PING_ATTEMPTS = 1

    # Integer: Minimum percent of the pings that must succeed to decide "host is up"
    PERCENT_SUCCESS_FOR_UP = 90
