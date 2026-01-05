log_path="python-works\\file_works\\system_logs\\logs.txt"
warning_path="python-works\\file_works\\system_logs\\warning.txt"
info_path="python-works\\file_works\\system_logs\\info.txt"
error_path="python-works\\file_works\\system_logs\\error.txt"

fr_log=open(log_path,"r")
fw_warning=open(warning_path,"w")
fw_info=open(info_path,"w")
fw_error=open(error_path,"w")

for line in fr_log:
    log=line.rstrip("\n")
    if "WARNING" in log:
        fw_warning.write(log+"\n")
    if "INFO" in log:
        fw_info.write(log+"\n")
    if "ERROR" in log:
        fw_error.write(log+"\n")

    """if log[log.find("WARNING")] == "W":
        fw_warning.write(log+"\n")
    elif log[log.find("INFO")] == "I":
        fw_info.write(log+"\n")
    elif log[log.find("ERROR")] == "E":
        fw_error.write(log+"\n")"""
    
print("program end")
fr_log.close()
fw_warning.close()
fw_info.close()
fw_error.close()
    