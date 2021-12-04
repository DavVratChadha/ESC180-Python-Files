#Reverse a string
def reverse_str(s):
    """Return the reversed verisionof string s"""
    reversed_str = ""
    #invariant: reversed_str is the reversed verion of
    #           s[:i] for interation i

    #reversed_str = "ba" (at interation 2)
    #               "c" + reversed_str

    for ch in s:
        reversed_str = ch + reversed_str
    return reversed_str

s = "abcde"
print(reverse_str(s))

#invariant: a condition that holds at every iteration of the loop

#Another way is to do this with slicing
s = "abcd"
s = s[::-1]
print(s)

##########
#anagrams
#"dcf ba" is an anagram of "abcdf"
#"dcff ba" is not an anagram of "a bc df"
#"ab" is anagram of "ba"
def is_anagram(s1,s2):
    s1 = s1.replace(" ", "")#get rid of spaces
    s2 = s2.replace(" ", "")
    for ch is s1 + s2:
        if s1.count(ch) != s2.count(ch):
            return False
    return True

print(is_anagram("praxis rule","lax surprise")) #True
print(is_anagram("abdh","h dbc a")) #False

#another way
def is_anagram2(s1,s2):
    s1 = sorted(s1.replace(" ", ""))
    s2 = sorted(s2.replace(" ", ""))
    if s1 != s2:
        return False
    return True

print(is_anagram2("praxis rule","lax surprise")) #True
print(is_anagram2("abdh","h dbc a")) #False

###########33
#a router needs to reciev N data packets(represent them as strings), and needs to transmit one of the N packets, uniformly at random (i.e., each packet should have an equal probability of being transmitted.
def send_packets(packet, N):
    #global all_packets?
    #No, because we did no moldify all_packets, ie.
    #we did not say all_packets = [*some_new_list*]
    #instead, we only change the value inside the list
    #so, we do not need global

    all_packets.append(packet)

    if len(all_packets) == N:
        n = int(N * random.random())
        return all_packet(n)


#How do you do the same thing of sending packets uniformly at random without storing the packets in all_packets?

def send_packets2(packet, N, all_packets):
    all_packets.append(packet)

    if len(all_packets) == N:
        n = int(N * random.random())
        return all_packets(n)


if __name__ == "__main__":
    all_packets = []
    print(send_packet("abc",3)) #none, coz all_pacekets has only 1 elem
    print(send_packet("def",3)) #none, coz all_pacekets has only 1 elem
    print(send_packet("ghi",3)) #abc, coz N == 3 == number of ele in all_packets