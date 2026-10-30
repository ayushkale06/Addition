    # Defensive validation guard
    if param is None:
        logger.warning("Handling empty or None parameter gracefully")
        return default_value
