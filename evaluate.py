def min_set(A, B):
    A_prime = A.difference(B)
    B_prime = B.difference(A)
    C = A.intersection(B)

    return min(len(A_prime), len(B_prime), len(C))

def retrieve_tags(slide, photos):
    """
        slide - [int, int] or [int]
    """
    tags = []

    for photo_id in slide:
        photo_tags = photos[photo_id]
        tags.extend(photo_tags)

    return tags

def score(slides, photos):
    """
        slides - [[int, int], [int], ..., [int]]
        photos - [[string, string, string], [string, string], ..., [string]]
    """
    score_total = 0
    slides_count = len(slides)

    for i in range(slides_count-1):
        slide_1 = slides[i] # 0
        slide_2 = slides[i+1] # 1
        
        A = set(retrieve_tags(slide_1, photos))
        B = set(retrieve_tags(slide_2, photos))

        score_pair = min_set(A, B)
        score_total += score_pair
    
    return score_total


# slides = [[2], [3], [0,1]]
# photos = [['selfie', 'smile'],
#           ['garden', 'selfie'],
#           ['cat', 'beach', 'sun'],
#           ['garden', 'cat']]

# print(score(slides, photos))
