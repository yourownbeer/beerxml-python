from beerxml.recipe import Recipe
import xmltodict


class BeerxmlParser:
    def parse(self, xml_content: str) -> Recipe:
        return Recipe(**xmltodict.parse(xml_content)["RECIPES"]["RECIPE"])
