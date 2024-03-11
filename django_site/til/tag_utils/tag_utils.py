from til.models import LearningTag


class TildeblogValueError(ValueError):
    def __init__(self, message):
        super(TildeblogValueError, self).__init__(message)


class TildeblogRuntimeError(RuntimeError):
    def __init__(self, message):
        super(TildeblogRuntimeError, self).__init__(message)


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
        :return: the id of the tag
        This wraps django object Manager get_or_create method to return just the id
        and raise an exception if the tag isn't cleaned beforehand
        """
        first_tag = self.split_tags(tagstring)[0]
        if first_tag != tagstring:
            raise TildeblogValueError(f"tagstring {tagstring} is not a valid tag")
        try:
            return LearningTag.objects.get_or_create(name=tagstring)[0].id
        except Exception as e:
            raise TildeblogRuntimeError(
                f"Excetion while trying to add {tagstring} to tags. \n:{e}"
            )
