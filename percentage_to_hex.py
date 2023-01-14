## need to fix colour mappings
def percentage_to_hex(percentage):
    # Map percentage to a value between 0 and 255
    value = int(percentage * 2.55)
    # Convert the value to hexadecimal and pad with a leading zero if necessary
    hex_value = hex(value)[2:].zfill(2)
    # Create a hexadecimal string with the RGB value
    hex_string = '#FF' + hex_value + hex_value
    return hex_string
