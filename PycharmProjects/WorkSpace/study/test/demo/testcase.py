#coding:utf-8

# 测试报告邮件内容
text = ""
# 用例统计
num_success = 0
num_fail = 0

# 测试通过
def test_success():
    global num_success
    num_success += 1
    print_out(u"测试结果：通过\n")


# 测试不通过
def test_fail(txt):
    global num_fail
    num_fail += 1
    print_out(u"测试结果：不通过 \n错误信息： " + txt + "\n")


# 邮件内容写入 & 客户端输出
def print_out(message):
    global text
    text += "\n" + message

# 返回值判断
def test_result(result, code):
    if result.get("status") == code:
        test_success()
        return "pass"
    else:
        txt = u"期望返回值:" + str(code) + u" 实际返回值:" + str(result.get("status"))
        test_fail(txt)
        return "fail"