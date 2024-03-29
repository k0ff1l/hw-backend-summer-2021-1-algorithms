__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    """Реализует текстовое представление времени.

    Example:
        >> seconds_to_str(20)
        20s
        >> seconds_to_str(60)
        01m00s
        >> seconds_to_str(65)
        01m05s
        >> seconds_to_str(3700)
        01h01m40s
        >> seconds_to_str(93600)
        01d02h00m00s
    """

    time_parts = []

    for divisor, time  in [(24 * 3600, 'd'), (3600, 'h'), (60, 'm'), (1, 's')]:
        value, seconds = divmod(seconds, divisor)
        if value or time_parts:
            time_parts.append(f'{value:02}{time}')

    if not time_parts:
        return "00s"

    return ''.join(time_parts)
