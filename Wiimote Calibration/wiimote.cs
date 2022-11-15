/** Wiimote Script. 
* 
* NOTE: This only works w/ GlovePIE & a 
* bluetooth connected wiimote.
* 
* @author Sean 
* @version 11/15/2022, 1:28am 
*/

GlovePIE.FrameRate = 125hz

var.screen_x = 1920 
var.screen_y = 1080

if wiimote.a {
   Mouse.X =  (var.wheel_degree / 360) //  * var.screen_x) )
   mouse.Y =  ((var.screen_y / 2) / var.screen_y)

   var.wheel_x = (wiimote.RawAccX)
   var.wheel_y = (wiimote.RawAccZ) + 0.01

   if (var.wheel_x > 0 && var.wheel_y > 0) { //---> QUADRANT I
     var.wheel_degree = int (Math.Atan(var.wheel_y / var.wheel_x))
   } else if (var.wheel_x < 0 && var.wheel_y > 0) { //---> QUADRANT II
     var.wheel_degree = int (Math.Atan(var.wheel_y / var.wheel_x) + 180)
   } else if (var.wheel_x < 0 && var.wheel_y < 0) { //---> QUADRANT III
     var.wheel_degree = int (Math.Atan(var.wheel_y / var.wheel_x) + 180)
   } else if (var.wheel_x > 0 && var.wheel_y < 0) { //---> QUADRANT IV
     var.wheel_degree = int (Math.Atan(var.wheel_y / var.wheel_x) + 360)
   }
}