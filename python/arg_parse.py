import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name',
                   type=str,
                   help='name')

# bool类型不能正确转换，传入字符串都为true, type可指定函数，转换字符串为bool类型
parser.add_argument('--gender',
                   type=bool,
                   help='True for male, False for female')

parser.add_argument('--gender2',
                   type=lambda x: x.lower() in ['true', '1'],
                   help='True for male, False for female')

args = parser.parse_args()
print('name is %s, type is %s' % (args.name, type(args.name))) 
print('gender is %s, type is %s' % (args.gender, type(args.gender)))
print('gender2 is %s, type is %s' % (args.gender2, type(args.gender2)))