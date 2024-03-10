from til.models import LearningTag


class TagHelper:
    def __init__(self, delim=","):
        # TODO make delim default from app settings
        self.delim = delim
        self.downcase_all = True

    def split_tags(self, tagstring: str) -> list:
        """
        Return a list of normalized, stripped strings
        :param tagstring: input string
        :return: the list of tags as strings
        """
        candidate_tags = tagstring.split(self.delim)
        no_empties = [x.strip() for x in candidate_tags if x.strip()]
        if self.downcase_all:
            retval = [x.lower() for x in no_empties]
        return list(set(retval))

    def get_new_or_existing_tag_id(self, tagstring: str) -> int:
        """
        Return the id for a tag.  If it doesn't exist already, create it.
        :param tagstring: valid string, should already be cleaned via split_tags
        :return:
        """
        first_tag = self.split_tags(tagstring)[0]
        if first_tag != tagstring:
            raise ValueError(f"tagstring {tagstring} is not a valid tag")
        try:
            return LearningTag.objects.get(name__exact=first_tag)
        except LearningTag.DoesNotExist:
            try:
                obj = LearningTag.objects.create(name=tagstring)
                return obj.id
            except Exception as InsertFailure:
                # conceivably it got insterted in the meantime
                try:
                    return LearningTag.objects.get(name__exact=first_tag)
                except Exception as e:
                    raise RuntimeError(
                        f"Unable to get or create {tagstring}:\n{InsertFailure} on attempted insert and"
                        f"{e} on retried get."
                    )
