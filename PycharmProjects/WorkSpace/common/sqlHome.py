
class SqlHome:
    """ 查询验证码 """
    @staticmethod
    def queryMessageCode_sql(phone):
        queryMessageCode_sql = {"receiver": ""+ phone + ""}
        return queryMessageCode_sql

    """ 查询登录表信息 """
    @staticmethod
    def queryLoginData_sql(loginName):
        queryLoginData_sql ="SELECT * FROM usercenter.u_user_login l WHERE l.login_name = '"+loginName+"'"
        return queryLoginData_sql

    """ 根据loginID删除用户信息 """
    @staticmethod
    def delLoginUser_sql(loginId):
        delLoginUser_sql = "DELETE FROM usercenter.u_user_login l WHERE l.login_id = '"+loginId+"'"
        return delLoginUser_sql

    """ 根据loginName删除用户信息 """
    @staticmethod
    def delLoginUserByLoginName_sql(loginName):
        delLoginUser_sql = "DELETE FROM usercenter.u_user_login l WHERE l.login_name ='"+loginName+"'"
        return delLoginUser_sql

    """ 根据loginID删除注册表司机信息 """
    @staticmethod
    def delRgtDriverByLoginID_sql(loginId):
        delRgtDriverByLoginID_sql = "DELETE FROM usercenter.uc_rgt_driver d WHERE d.login_id = '"+loginId+"'"
        return delRgtDriverByLoginID_sql

    """ 根据loginID删除注册表车辆信息 """
    @staticmethod
    def delRgtVehicle_sql(loginId):
        delRgtVehicle_sql = "DELETE FROM usercenter.uc_rgt_vehicle v WHERE v.login_id = '"+loginId+"'"
        return delRgtVehicle_sql

    """ 根据身份证和司机姓名删除司机注册表信息 """
    @staticmethod
    def delRgtDriver_sql(idNum,driverName):
        delRgtDriver_sql = "DELETE FROM usercenter.uc_rgt_driver d WHERE d.id_num = '"+idNum+"'OR d.driver_name = '"+driverName+"'"
        return delRgtDriver_sql

    """ 根据身份证删除身份证拓展表信息 """
    @staticmethod
    def delDriver_cert_d_sql(idNum):
        delDriver_cert_d_sql = "DELETE FROM usercenter.uc_driver_cert_d dd WHERE dd.driver_cert_id = (SELECT dc.driver_cert_id FROM usercenter.uc_driver_cert dc WHERE dc.driver_id_num = '"+idNum+"')"
        return delDriver_cert_d_sql

    """ 根据身份证删除身份证表信息 """
    @staticmethod
    def delDriver_cert_sql(idNum):
        delDriver_cert_sql = "DELETE FROM usercenter.uc_driver_cert dc WHERE dc.driver_id_num = '"+idNum+"'"
        return delDriver_cert_sql

    """ 根据身份证删除司机主表信息 """
    @staticmethod
    def delDriverByIdNum_sql(idNum):
        delDriverByIdNum_sql = "DELETE FROM usercenter.uc_driver d WHERE d.id_num = '"+idNum+"'"
        return delDriverByIdNum_sql
    """ 根据手机号删除司机主表信息 """
    @staticmethod
    def delDriverByPhone_sql(phone):
        delDriverByPhone_sql = "DELETE FROM usercenter.uc_driver d WHERE d.phone = '"+phone+"'"
        return delDriverByPhone_sql

    """ 根据手机号查询注册表司机和车辆的审核状态 """
    @staticmethod
    def query_auditStatus_sql(phone):
        query_auditStatus_sql = "SELECT d.audit_status,v.audited_status FROM usercenter.u_user_login l,usercenter.uc_rgt_driver d,usercenter.uc_rgt_vehicle v WHERE l.login_name = d.phone AND d.login_id = v.login_id AND v.login_id = (SELECT rd.login_id FROM usercenter.uc_rgt_driver rd WHERE rd.phone = '"+phone+"')"
        return query_auditStatus_sql

    """ 查询可以做业务的司机 """
    @staticmethod
    def query_UseDriver_sql():
        query_UseDriver_sql = "SELECT b.login_name,b.passwd,a.driver_id,v.vehicle_id FROM usercenter.uc_driver a,usercenter.u_user_login b,usercenter.uc_vehicle v WHERE a.vehicle_id = v.vehicle_id AND v.val_status = '1' AND a.driver_id = b.user_id AND b.val_status = '1' AND b.user_type = '1' AND a.val_status = '1' AND (SELECT COUNT(*) FROM usercenter.uc_driver_bank_card k WHERE k.driver_id = a.driver_id   AND k.authority_flag = '1') >=1 AND (SELECT COUNT(*) from business.bu_delivery de where de.vehicle_id = v.vehicle_id and de.val_status>'05' and de.val_status<'90')= 0 AND (SELECT COUNT(*) from business.bu_delivery de where de.driver_id = a.driver_id and de.val_status>'05' and de.val_status<'90')= 0 AND a.plat_source = 'WBKJ'AND b.passwd = '111111' GROUP BY v.vehicle_id ORDER BY a.created_time DESC LIMIT 2"
        return query_UseDriver_sql

    """ 查询生效的司机和车辆 """
    @staticmethod
    def query_driverAndVehicle_sql(num):
        query_driverAndVehicle_sql = "SELECT d.driver_id,v.vehicle_id FROM usercenter.uc_driver d,usercenter.uc_vehicle v WHERE d.val_status =1 AND v.val_status =1 AND d.vehicle_id = v.vehicle_id ORDER BY v.created_time DESC LIMIT "+str(num)+""
        return query_driverAndVehicle_sql

    """ 删除物流公司注册表信息 """
    @staticmethod
    def delRgtLogisByLoginName_sql(loginName):
        delRgtLogisByLoginName_sql = "DELETE FROM usercenter.uc_rgt_logis l WHERE l.login_id = (SELECT l.login_id FROM usercenter.u_user_login l WHERE l.login_name ='"+loginName+"')"
        return delRgtLogisByLoginName_sql

    """ 删除物流公司主表信息 """
    @staticmethod
    def delLogis_sql(logisName):
        delLogis_sql = "DELETE FROM usercenter.uc_logis l WHERE l.logis_name = '"+logisName+"'"
        return delLogis_sql

    """ 删除物流公司注册表信息 """
    @staticmethod
    def delRgtLogisByLogisName_sql(logisName):
        delRgtLogisByLogisName_sql = "DELETE FROM usercenter.uc_rgt_logis l WHERE l.logis_name ='"+logisName+"'"
        return delRgtLogisByLogisName_sql

    """ 查询物流公司审核状态 """
    @staticmethod
    def queryLogisAuditStatus__sql(logisName):
        queryLogisAuditStatus__sql = "SELECT * FROM usercenter.uc_rgt_logis l WHERE l.logis_name = '"+logisName+"'"
        return queryLogisAuditStatus__sql

    """ 查询最近的一条货源单数据 """
    @staticmethod
    def queryPublish_sql():
        queryPublish_sql ="SELECT * FROM business.bu_publish p ORDER BY p.publish_id DESC LIMIT 1"
        return queryPublish_sql

    """ 因为手动添加数据 所以需要先查到数据 """
    @staticmethod
    def query_insertData_sql(out_business_id):
        query_insertData_sql = "SELECT r.if_polling,r.out_business_id,r.flow_no,r.id_num,r.platform_order_no from financecenter.pm_bank_response r where r.out_business_id ='"+out_business_id+"';"
        return query_insertData_sql

    """ 为了支付成功  pm_bank_pay_result手动添加数据 """
    @staticmethod
    def insert_to_PmBankPayResult_sql(out_business_id,channel_flow_no,id_num,platform_order_no,recv_acct_no):
        insert_to_PmBankPayResult_sql = "INSERT INTO financecenter.pm_bank_pay_result(out_business_id, channel_flow_no,recva_acct_type,result_code,result_desc,unify_result_code,unify_result_desc,pay_institution_flag,id_num,created_time,cash_flow_no,platform_order_no,plat_type,result_amount,pay_amount,recv_acct_no,order_no) VALUES ("+out_business_id+",'"+channel_flow_no+"','0','3','支付成功','0','支付成功','97','"+id_num+"','2021-07-15 13:02:33','','"+platform_order_no+"','2',1390.00,1390.00,'"+recv_acct_no+"','');"
        return insert_to_PmBankPayResult_sql

    """ 为了支付成功 pm_bank_response修改if_polling=1 """
    @staticmethod
    def update_to_PmBankResponse_sql(out_business_id):
        update_to_PmBankResponse_sql = "UPDATE financecenter.pm_bank_response SET if_polling= 1 WHERE out_business_id = "+out_business_id+""
        return update_to_PmBankResponse_sql

    """ 查询调度单的 delivery_pay_id"""
    @staticmethod
    def query_deliveryPayId_sql(delivery_id):
        query_deliveryPayId_sql = "SELECT p.delivery_pay_id FROM financecenter.fi_delivery_pay p WHERE p.delivery_id = "+delivery_id+""
        return query_deliveryPayId_sql

    """ 查询调度单的付款请求的轮询状态 if_do_withed 和 银行卡号 recv_acct_no """
    @staticmethod
    def query_deliveryPayReq_sql(zf_child_id):
        query_deliveryPayReq_sql = "SELECT r.if_do_withed,r.recv_acct_no FROM financecenter.fi_pay_req r WHERE r.zf_child_id IN ('"+zf_child_id+"')"
        return query_deliveryPayReq_sql

    """ 查询正式表司机信息 """
    @staticmethod
    def query_driver_sql(phone):
        query_driver_sql = "SELECT * FROM usercenter.uc_driver d WHERE d.phone = "+phone+""
        return query_driver_sql

    """ 查询调度单状态 """
    @staticmethod
    def query_delivery_valStatus_sql(deliveryId):
        query_delivery_valStatus_sql = "SELECT d.* FROM business.bu_delivery d WHERE d.delivery_id = '"+str(deliveryId)+"'"
        return query_delivery_valStatus_sql

    """ 修改调度单状态 """
    @staticmethod
    def update_delivery_valStatus_byDriverId(driver_id,val_status='00'):
        update_delivery_valStatus_sql = "UPDATE business.bu_delivery d SET d.val_status = '"+val_status+"' WHERE d.driver_id = '"+str(driver_id)+"' AND d.val_status NOT IN ('00','90')"
        return update_delivery_valStatus_sql

    """ 修改调度单状态 """

    @staticmethod
    def update_delivery_valStatus_byLoginName(login_name, val_status='00'):
        update_delivery_valStatus_sql = "UPDATE business.bu_delivery d SET d.val_status = '"+val_status+"' WHERE d.driver_id = ((SELECT d.driver_id FROM usercenter.uc_driver d WHERE d.driver_id = (SELECT l.user_id FROM usercenter.u_user_login l WHERE l.login_name = '"+login_name+"'))) AND d.val_status NOT IN ('00','90')"
        return update_delivery_valStatus_sql

    """ 删除货主主表信息 """
    @staticmethod
    def delOwnerByOwnerName_sql(ownerName):
        delOwnerByOwnerName_sql= "DELETE FROM usercenter.uo_owner o WHERE o.owner_name = '"+ownerName+"'"
        return delOwnerByOwnerName_sql

    """ 删除货主注册表信息 """
    @staticmethod
    def delRgtOwner_sql(loginName,ownerName):
        delRgtOwner_sql= "DELETE FROM usercenter.uo_rgt_owner o WHERE o.login_name = '"+loginName+"' OR o.owner_name = '"+ownerName+"'"
        return delRgtOwner_sql

    """ 查询货主审核状态 """
    @staticmethod
    def queryOwnerAuditStatus__sql(ownerName):
        queryOwnerAuditStatus__sql = "SELECT * FROM usercenter.uo_rgt_owner o WHERE o.owner_name = '"+ownerName+"'"
        return queryOwnerAuditStatus__sql

    """ 修改货主登录密码 """
    @staticmethod
    def update_ownerPassword_sql(loginName):
        update_ownerPassword_sql = " UPDATE usercenter.u_user_login l SET l.passwd = 111111 WHERE l.login_name = '"+loginName+"'"
        return update_ownerPassword_sql

    """ 查询货源单信息 """
    @staticmethod
    def query_publishByPublishId_sql(publishId):
        query_publishByPublishId_sql = "SELECT p.detachable,p.appoint_team_type,p.appoint_team_id,p.fee_flag,p.fee_amount,p.goods_insurance_flag,p.if_audit,p.* FROM business.bu_publish p WHERE p.publish_id = '"+str(publishId)+"'"
        return query_publishByPublishId_sql

    """ 查询ownerId """
    @staticmethod
    def query_ownerId_sql(loginName):
        query_ownerId_sql = "SELECT u.owner_id FROM usercenter.uo_owner_user u WHERE u.owner_user_id = (SELECT l.user_id FROM usercenter.u_user_login l WHERE l.login_name = '"+loginName+"')"
        return query_ownerId_sql

    """ 查询ownerId对应的税率模式服务费配置信息 """
    @staticmethod
    def query_ownerTax_fee_sql(owner_id):
        query_ownerTax_fee_sql = "SELECT * FROM usercenter.uo_owner_tax_fee_config c WHERE c.owner_id = '"+str(owner_id)+"'"
        return query_ownerTax_fee_sql

    """ 查询ownerId对应的货运险配置信息 """
    @staticmethod
    def query_owner_goods_insurance_sql(owner_id):
        query_owner_goods_insurance_sql = "SELECT * FROM usercenter.uo_owner_goods_insurance_config c WHERE c.owner_id = '"+str(owner_id)+"'"
        return query_owner_goods_insurance_sql

    """ 查询ownerId对应的最高补助金配置信息 """
    @staticmethod
    def query_owner_max_rebate_amount_sql(owner_id):
        query_owner_max_rebate_amount_sql = "SELECT * FROM financecenter.uo_max_rebate_amount_config o WHERE o.owner_id = '"+str(owner_id)+"'"
        return query_owner_max_rebate_amount_sql

    @staticmethod
    def query_rgtVehicleNum_sql(login_id):
        query_rgtVehicleNum_sql = "SELECT * FROM usercenter.uc_rgt_vehicle v WHERE v.login_id = '"+str(login_id)+"'"
        return query_rgtVehicleNum_sql

    @staticmethod
    def query_publishIdByDependId(dependId):
        query_publishIdByDependId_sql = "SELECT * FROM business.bu_publish p WHERE p.depend_id = '"+str(dependId)+"'AND p.ext_plat_code = 'changhong.com' ORDER BY p.created_time DESC LIMIT 1"
        return query_publishIdByDependId_sql

    @staticmethod
    def query_deliveryIdByPublishId(publishId):
        query_deliveryIdByPublishId_sql = "SELECT * FROM business.bu_delivery d WHERE d.publish_id = '"+str(publishId)+"' ORDER BY d.created_time DESC LIMIT 1"
        return query_deliveryIdByPublishId_sql
