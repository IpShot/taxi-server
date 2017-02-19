##
# Searching the element index in the list by id
#
def find_idx_by_id(l, id):
	return next(
		(i for i, x in enumerate(l) if x.id == id), 
		None,
	)