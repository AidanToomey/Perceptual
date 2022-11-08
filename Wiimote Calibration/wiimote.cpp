GlovePIE.FrameRate = 125hz

// "w" = WHEEL

var.gyro_Raw = 0
var.wP = 0
var.wP_Raw = 0

if wiimote.a {
   //Mouse.DirectInputX += sin(atan2(wiimote.MotionPlus.RawYawSpeed/ 125, -wiimote.MotionPlus.RawPitchSpeed/125)) * |( wiimote.MotionPlus.RawYawSpeed/ 125)| * 30
   var.wP_Raw += sin(atan2(wiimote.MotionPlus.RawYawSpeed/ 125, -wiimote.MotionPlus.RawPitchSpeed/125)) * |( wiimote.MotionPlus.RawYawSpeed/ 125)| * 30

   //Mouse.CursorPosX =
   var.gyro_Raw = wiimote.MotionPlus.GyroYaw

} else {
  debug = "Testing paused - setting position to 0"
  Mouse.CursorPosX = 0
}