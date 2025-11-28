invitees = ["나재헌", "나루", "아이유", "메시", "호날두"]
companionsCnt = [1, 3, 4, 0, 2]

print("총 참석 인원: ", sum(companionsCnt) + len(invitees))
print("한 사람이라도 동반자가 존재하는지 여부: ", any(companionsCnt))
print("모든 사람이 동반자를 동반하는지 여부: ", all(companionsCnt))
print("가장 많은 동반자 수: ", max(companionsCnt))
for invitee, companionsCnt in zip(invitees, companionsCnt):
    print(invitee, companionsCnt, end=" ")