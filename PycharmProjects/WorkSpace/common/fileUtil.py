""" 文件操作基类  """
class FileUtils:

    """ 用于司机注册,获取不同照片的路径 """
    @staticmethod
    def get_FilePath(picType,if_hand_car=0):
        id_font_pic = 'C:/Users/xhx14/Desktop/所有文档/00-公司/00-02-脚本/脚本/python/WorkSpace/common/pic/ZM.jpg'
        id_back_pic = 'C:/Users/xhx14/Desktop/所有文档/00-公司/00-02-脚本/脚本/python/WorkSpace/common/pic/FM.jpg'
        jsz_pic     = 'C:/Users/xhx14/Desktop/所有文档/00-公司/00-02-脚本/脚本/python/WorkSpace/common/pic/jsz.jpg'
        zcxsz_pic   = 'C:/Users/xhx14/Desktop/所有文档/00-公司/00-02-脚本/脚本/python/WorkSpace/common/pic/行驶证0139.jpg'
        clzmz_pic   = 'C:/Users/xhx14/Desktop/所有文档/00-公司/00-02-脚本/脚本/python/WorkSpace/common/pic/clzmz.jpg'
        qm_pic      = 'C:/Users/xhx14/Desktop/所有文档/00-公司/00-02-脚本/脚本/python/WorkSpace/common/pic/qm.jpg'
        zcysz_pic   = 'C:/Users/xhx14/Desktop/所有文档/00-公司/00-02-脚本/脚本/python/WorkSpace/common/pic/zcysz.jpg'
        cyzgz_pic   = 'C:/Users/xhx14/Desktop/所有文档/00-公司/00-02-脚本/脚本/python/WorkSpace/common/pic/cyzgz.jpg'
        gcxsz_pic   = 'C:/Users/xhx14/Desktop/所有文档/00-公司/00-02-脚本/脚本/python/WorkSpace/common/pic/xsz.jpg'
        gcysz_pic   = 'C:/Users/xhx14/Desktop/所有文档/00-公司/00-02-脚本/脚本/python/WorkSpace/common/pic/qt.jpg'
        if picType == 1:
            return id_font_pic  # 身份证正面
        elif picType == 2:
            return id_back_pic   # 身份证反面
        elif picType == 3:
            return jsz_pic   # 驾驶证
        elif picType == 4:
            return zcxsz_pic   # 行驶证
        elif picType == 5:
            return zcysz_pic  # 主车道路运输证
        elif picType == 6:
            return clzmz_pic  # 车辆正面照
        elif picType == 11:
            return qm_pic   # 签名图片
        elif picType == 13:
            return cyzgz_pic   # 从业资格证
        elif picType == 9 and if_hand_car == 1:
            return gcysz_pic   # 挂车道路运输证
        elif picType == 10 and if_hand_car == 1:
            return gcxsz_pic   # 挂车行驶证
        else:
            raise Exception("\033[31m未匹配到合适的图片类型!!!")

    """ 用于回单上传,获取不同照片的路径 """
    @staticmethod
    def get_PicPath():
        hd_pic = 'C:/Users/xhx14/Desktop/所有文档/00-公司/00-02-脚本/脚本/python/WorkSpace/common/pic/qm.jpg' # 回单图片
        if hd_pic :
            return hd_pic
        else:
            raise Exception("\033[31m未匹配到合适的图片类型!!!")







