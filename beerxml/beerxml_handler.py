from beerxml.recipe import Recipe
import xmltodict


class BeerxmlParser:
    def __init__(self, xml_content):
        self._xml_content = xml_content

    def parse(self) -> Recipe:
        return Recipe(**xmltodict.parse(self._xml_content)["RECIPES"]["RECIPE"])
