from datetime import datetime
caller_id = 0
class Call(object):
    def __init__(self,caller_id,caller_name,call_phnumber,call_reason):
        self.caller_id = caller_id
        self.caller_name = caller_name
        self.call_phnumber = call_phnumber
        self.call_time = datetime.now()
        self.call_reason = call_reason

        caller_id = caller_id + 1


    def display(self):
        print "caller id: {}".format(self.caller_id)
        print "caller name: {}".format(self.caller_name)
        print "caller phone number: {}".format(self.call_phnumber)
        print "time of the call: {}".format(self.call_time)
        print "reason for call: {}".format(self.call_reason)
        return self

# call1 = Call(1,"jon",4089671234,"login not working")
# # call1.display()
# call2 = Call(2,"wick",4081234567,"balance enquiry")
# # call2.display()

class Callcenter(object):
    def __init__(self):
        self.number_calls = []

    def current_queue_size(self):
        return len(self.number_calls)

    def add(self,call):
        self.number_calls.append(call)
        return self

    def remove(self):
        del self.number_calls[0]
        return self

    def info(self):
        for call in self.number_calls:
            call.display()

center = Callcenter()
center.add(Call(1, "jon", "1234567890", "login"))
center.add(Call(2, "wick", "2345678901", "registration"))
center.add(Call(3, "jane", "3456789012", "balance"))
center.add(Call(4, "doe", "45678901234", "savings"))
center.info()

center.remove().info()
