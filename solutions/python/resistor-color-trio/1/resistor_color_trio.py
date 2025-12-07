colours = {"black":0, "brown":1, "red":2, "orange":3, "yellow":4, "green":5, "blue":6, "violet":7, "grey":8, "white":9}
def label(colors):
    value = (colours[colors[0]]*10 + colours[colors[1]]) * 10**colours[colors[2]]
    if value >= 1000000000:
        value = str(value//1000000000) + ' gigaohms'
        return value
    if value >= 1000000:
        value = str(value//1000000) + ' megaohms'
        return value
    if value >= 1000:
        value = str(value//1000) + ' kiloohms'
        return value
    return str(value)+' ohms'
    