from ctypes import util
import utils

driver_path = "C:\\Users\\JHONAS\\Documents\\APEC-20220124T004744Z-001\\APEC\\Cuatrimestre 10\\Calidad\\robot_process_automation_onedrive_file\\driver\\chromedriver.exe"
drive_url = "https://www.office.com/"



sign_in_selector = utils.replace_whitespace_with_dot("mectrl_header_text mectrl_truncate x-hidden-focus")
next_button_selector = utils.replace_whitespace_with_dot("input.win-button button_primary button ext-button primary ext-primary")
yes_button_selector = utils.replace_whitespace_with_dot("input.win-button button_primary button ext-button primary ext-primary")

