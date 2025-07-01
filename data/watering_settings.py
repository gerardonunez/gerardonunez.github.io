def get_online_settings():
    # --- Durations (in seconds) ---
    settings = dict()
    settings["BOOT_DURATION"] = 5 * 60       # 5 minutes at boot
    settings["SMALL_DURATION"] = 1 * 60      # 2 minutes
    settings["LARGE_DURATION"] = 1 * 60      # 3 minutes

    # --- Watering Schedule ---
    # Small: 19h00  UTC = 21h00 France
    # Large: 19h10  UTC = 21h10 France
    settings["SMALL_HOUR"] = 17 - 2
    settings["SMALL_MIN"] = 31
    settings["LARGE_HOUR"] = 21 - 2 
    settings["LARGE_MIN"] = 10

    # --- Watering frequency ---
    settings["SMALL_PERIOD"] = 2    # One day watering, one day off
    settings["LARGE_PERIOD"] = 3    # One day watering, two days off
    return settings
