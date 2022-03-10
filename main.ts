radio.setGroup(1)
//  1 až 255
radio.setTransmitPower(7)
//  0 až 7 vysílací hodnoty
let data_list = []
basic.forever(function on_forever() {
    
})
radio.sendValue("name", 0)
// jednorázový příjem proměných
// X
radio.onReceivedValue(function data_received(name: string, value: number) {
    
})
