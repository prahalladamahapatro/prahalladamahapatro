colours = {"black":0, "brown":1, "red":2, "orange":3, "yellow":4, "green":5, "blue":6, "violet":7, "grey":8, "white":9}
tolerance = { 'grey':'±0.05%', 'violet':'±0.1%', 'blue':'±0.25%', 'green':'±0.5%', 'brown':'±1%', 'red':'±2%', 'gold':'±5%', 'silver':'±10%' }
# metric prefixes in descending order
units = [ (1_000_000_000, "gigaohms"), (1_000_000, "megaohms"), (1_000, "kiloohms") ]


def clean_number(x):
    """Return integer if whole, else float without trailing zeros."""
    if x.is_integer():
        return str(int(x))
    else:
        return str(x).rstrip('0').rstrip('.')
        
def resistor_label(colors):
    if len(colors) == 1:
        return str(colours[colors[0]]) + ' ohms'
    if len(colors) == 4:
        value = (colours[colors[0]]*10 + colours[colors[1]]) * 10**colours[colors[-2]]
    if len(colors) == 5:
        value = (colours[colors[0]]*100 + colours[colors[1]]*10 + colours[colors[2]]) * 10**colours[colors[-2]]
    
    '''if value >= 1000000000:
        value = clean_number(value/1000000000) + ' gigaohms ' + tolerance[colors[-1]]
        return value
    if value >= 1000000:
        value = clean_number(value/1000000) + ' megaohms ' + tolerance[colors[-1]]
        return value
    if value >= 1000:
        value = clean_number(value/1000) + ' kiloohms ' + tolerance[colors[-1]]
        return value'''

    for factor, name in units:
        if value >= factor:
            return f"{clean_number(value/factor)} {name} {tolerance[colors[-1]]}"
    return str(value)+' ohms ' + tolerance[colors[-1]]
