import lib.globalvar as gl
import lib.ulits as ulits
import lib.settings as settings

def main():  
  ulits.connect()
  gl.set('times', 0)
  courseId = gl.get('courseId')
  while True:
    try:
      if ulits.auto_snap(courseId): break
    except:
      continue
  gl.get('driver').close()
  print('quit')

if __name__ == "__main__":
  version = '1.0.0@142441'
  Time = 'Sat Jun  5 01:55:02 2021'
  f = open('./user.txt')
  gl._init()
  gl.set('username', f.readline().strip())
  gl.set('password', f.readline().strip())
  gl.set('courseId', f.readline().strip())
  gl.set('errorMessage', False)
  gl.set('timesCount', 1)
  gl.set('driver' , settings._init())
  print(ulits.get_ctime())
