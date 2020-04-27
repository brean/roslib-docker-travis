roslib:
	docker-compose up roslib

talk_listen:
	# run just the talker and listener rosnodes to test the basic system
	# should output something like:
	#   talker_1    | [INFO] [1234567890.0]: hello world 1234567890.0
    #   listener_1  | [INFO] [1234567890.1]: /listenerI heard hello world 1234567890.0
	docker-compose up talker listener
