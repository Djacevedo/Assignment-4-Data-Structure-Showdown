# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
def removeDuplicatesKeepOrder(values):
    seen=set()
    result=[]
    for v in values:
        if v not in seen:
            result.append(v)
            seen.add(v)
            return result