# P53

import sys, os
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


def main():
	s=input()
	freq=dict()
	for i in s:
		s = s.lower()
		if i in freq:
			freq[i] +=1
		else:
			freq[i] = 1

	result=', '.join('{}:{}'.format(k,v) for k,v in freq.items())
	print(result)


if __name__ == "__main__":
    main()