from itertools import chain

from autocorrect.constants import alphabets


class Word:
    """container for word-based methods"""

    __slots__ = ["slices", "word", "alphabet", "only_replacements"]  # optimization

    def __init__(self, word, lang="ta", only_replacements=False):
        """
        Generate slices to assist with typo
        definitions.

        'the' => (('', 'the'), ('t', 'he'),
                  ('th', 'e'), ('the', ''))

        'வணக்கம்' => (('', 'வணக்கம்'), ('வ', 'ணக்கம்'), ('வண', 'க்கம்'),
                        ('வணக', '்கம்'), ('வணக்க', 'ம்'), ('வணக்கம', '்'),
                        ('வணக்கம்', ''))
          
        """
        slice_range = range(len(word) + 1)
        self.slices = tuple((word[:i], word[i:]) for i in slice_range)
        self.word = word
        self.alphabet = alphabets[lang]
        self.only_replacements = only_replacements

    def _deletes(self):
        """th"""
        for a, b in self.slices[:-1]:
            yield "".join((a, b[1:]))

    def _deletes(self):
        """வணகம்"""
        for a, b in self.slices[:-1]:
            yield "".join((a, b[1:]))

    def _transposes(self):
        """teh"""
        for a, b in self.slices[:-2]:
            yield "".join((a, b[1], b[0], b[2:]))

    def _transposes(self):
        """வணகக்ம்"""
        for a, b in self.slices[:-2]:
            yield "".join((a, b[1], b[0], b[2:]))

    def _replaces(self):
        """tge"""
        for a, b in self.slices[:-1]:
            for c in self.alphabet:
                yield "".join((a, c, b[1:]))

    def _replaces(self):
        """வணக்கண்"""
        for a, b in self.slices[:-1]:
            for c in self.alphabet:
                yield "".join((a, c, b[1:]))

    def _inserts(self):
        """thwe"""
        for a, b in self.slices:
            for c in self.alphabet:
                yield "".join((a, c, b))

    def _inserts(self):
        """வணக்கம்ம"""
        for a, b in self.slices:
            for c in self.alphabet:
                yield "".join((a, c, b))

    def typos(self):
        """letter combinations one typo away from word"""
        if self.only_replacements:
            return chain(self._replaces())
        else:
            return chain(
                self._deletes(), self._transposes(), self._replaces(), self._inserts()
            )
        
    def double_typos(self):
        """letter combinations two typos away from word"""
        return chain.from_iterable(
            Word(e1, only_replacements=self.only_replacements).typos()
            for e1 in self.typos()
        )