# AI algorithm

# Assess utility of current state
# For each available action
	# For each available set of targets
		# estimate future state from action
		# assess utility based on predicted state
		# store utility value for action
# convert raw utility values to probility distribution using softmax
# take action
# record immediate reward/state
# update model