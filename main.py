
radio.set_group(1) # 1 až 255
radio.set_transmit_power(7) # 0 až 7 vysílací hodnoty

data_list = []

def on_forever():
    pass
basic.forever(on_forever)


radio.send_value("name", 0) #jednorázový příjem proměných

#X

def data_received(name, value):
    pass
radio.on_received_value(data_received) #vždy když se něco stane

