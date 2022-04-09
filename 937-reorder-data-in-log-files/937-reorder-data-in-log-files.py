class Solution(object):
    def reorderLogFiles(self, logs):
        
        dig_logs = []
        let_logs = []

        for log in logs:
            log_splitted = log.split()
            ident = log_splitted[0]
            content = " ".join(log_splitted[1:])

            if(content[0].isalpha()):
                let_logs.append((content, ident, log))
            else:
                dig_logs.append(log)

        let_logs = sorted(let_logs, key=lambda x:(x[0], x[1]))

        return [log[2] for log in let_logs] + dig_logs

       