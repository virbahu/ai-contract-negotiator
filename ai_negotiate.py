import numpy as np
def calculate_negotiate_terms(our_position, their_position, priorities):
    terms = {}
    for key in our_position:
        our_val = our_position[key]; their_val = their_position.get(key, our_val)
        weight = priorities.get(key, 0.5)
        compromise = our_val * weight + their_val * (1 - weight)
        terms[key] = round(compromise, 2)
    satisfaction = sum(1 - abs(terms[k]-our_position[k])/max(abs(our_position[k]),1) for k in terms) / len(terms) * 100
    return {"proposed_terms": terms, "our_satisfaction_pct": round(satisfaction, 1)}
if __name__=="__main__":
    ours = {"price": 10, "volume": 5000, "lead_time": 14, "payment_days": 30}
    theirs = {"price": 12, "volume": 3000, "lead_time": 21, "payment_days": 60}
    prio = {"price": 0.7, "volume": 0.6, "lead_time": 0.8, "payment_days": 0.5}
    print(calculate_negotiate_terms(ours, theirs, prio))
