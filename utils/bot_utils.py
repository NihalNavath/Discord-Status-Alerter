from datetime import timedelta

def timedelta_to_humanreadable(downtime: timedelta):
    """Takes it of type timedelta and returns a human readable form in the 
    form 'd h m s'

    Args:
        downtime (timedelta): Time in timedelta

    Returns:
        [str]: Human readable time 
    """
    hours, remainder = divmod(int(downtime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    
    return (f"{days}d, {hours}h, {minutes}m, {seconds}s")

def mention_channel(channelids :list, separator: str):
    """Takes in a list of ids and turns it into channel pings, each mention is seprated
    by the argument 'separator'

    Args:
        channelids (list): The array containing the channel ids 
        separator (str): String to seprate the mentions

    Returns:
        [list]: The list containing the mentioned channels

    Example: mention_channel([1 , 2 ,3], ", ") -> [<#1>, <#2>, <#3>]
    """
    mapped_ids = (map(str , channelids))

    return separator.join([f"<#{id}>" for id in mapped_ids])

def mention_users(userids :list, separator: str):
    """Takes in a list of user ids and turns it into user pings, each mention is seprated
    by the argument 'separator'

    Args:
        userids (list): The list containing the user ids
        separator (str): String to seprate the mentions

    Returns:
        [list]: The list containing the mentioned users

    Example: mention_channel([1 , 2 ,3], ", ") -> [<@1>, <@2>, <@3>]
    """
    mapped_ids = (map(str , userids))

    return separator.join([f"<@{id}>" for id in mapped_ids])