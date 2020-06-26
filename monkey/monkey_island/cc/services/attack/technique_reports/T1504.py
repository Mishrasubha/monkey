from common.data.post_breach_consts import \
    POST_BREACH_SHELL_STARTUP_FILE_MODIFICATION
from common.utils.attack_utils import ScanStatus
from monkey_island.cc.database import mongo
from monkey_island.cc.services.attack.technique_reports import AttackTechnique

__author__ = "shreyamalviya"


class T1504(AttackTechnique):
    tech_id = "T1504"
    unscanned_msg = "Monkey did not try modifying powershell startup files on the system."
    scanned_msg = "Monkey tried modifying powershell startup files on the system but failed."
    used_msg = "Monkey modified powershell startup files on the system."

    query = [{'$match': {'telem_category': 'post_breach',
                         'data.name': POST_BREACH_SHELL_STARTUP_FILE_MODIFICATION}},
             {'$project': {'_id': 0,
                           'machine': {'hostname': '$data.hostname',
                                       'ips': ['$data.ip']},
                           'result': '$data.result'}}]

    @staticmethod
    def get_report_data():
        data = {'title': T1504.technique_title(), 'info': []}

        shell_startup_files_modification_info = list(mongo.db.telemetry.aggregate(T1504.query))

        powershell_startup_modification_info = []
        for shell_startup_file_result in shell_startup_files_modification_info[0]['result']:
            # only want powershell startup files
            if "profile.ps1" in shell_startup_file_result[0]:
                powershell_startup_modification_info.append({
                    'machine': shell_startup_files_modification_info[0]['machine'],
                    'result': shell_startup_file_result
                    })

        status = []
        for powershell_startup_file in powershell_startup_modification_info:
            status.append(powershell_startup_file['result'][1])
        status = (ScanStatus.USED.value if any(status) else ScanStatus.SCANNED.value)\
            if status else ScanStatus.UNSCANNED.value

        data.update(T1504.get_base_data_by_status(status))
        data.update({'info': powershell_startup_modification_info})
        return data
