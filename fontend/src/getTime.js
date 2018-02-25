export function getTime(){
    var date = new Date()
    var hyphen = "-"
    var colon = ":"
    var month = date.getMonth() + 1
    var day = date.getDate()
    var hour = date.getHours()
    var minutes = date.getMinutes()
    var seconds = date.getSeconds()
    if (month >= 1 && month <= 9) {
      month = "0" + month
    }
    if (day >= 0 && day <= 9) {
      day = "0" + day
    }
    if (hour >= 0 && hour <= 9) {
      hour = "0" + hour
    }
    if (minutes >= 0 && minutes <= 9) {
      minutes = "0" + minutes
    }
    if (seconds >= 0 && seconds <= 9) {
      seconds = "0" + seconds
    }
    var newDate = date.getFullYear() + hyphen + month + hyphen + day + " " + hour + colon + minutes + colon + seconds
    return newDate
  }