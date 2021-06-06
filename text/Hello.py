b = None
a = None
name = None
s = None
r = None


print('©Darkmoon,2020')
name = int(input('输入1则计算圆面积，输入2则计算正方形面积：'))
if name == 1:
  r = float(input('圆的半径：'))
  s = 3.14 * (r * r)
  print(str('圆的面积为：') + str(s))
  input('按Enter键退出')
elif name == 2:
  a = input('正方形边长：')
  b = int(a)*int(a)
  print(str('正方形面积为：') + str(b))
  input('按Enter键退出')
else:
  print('眼睛长屁股上了？看不到上面的字吗？')
  name = int(input('输入1则计算圆面积，输入2则计算正方形面积：'))
  if name == 1:
    r = float(input('圆的半径：'))
    s = 3.14 * (r * r)
    print(str('圆的面积为：') + str(s))
    input('按Enter键退出')
  elif name == 2:
    a = input('正方形边长：')
    b = int(a)*int(a)
    print(str('正方形面积为：') + str(b))
    input('按Enter键退出')
  else:
    input('救不了你了，按Enter键退出')
