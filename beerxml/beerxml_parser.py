from beerxml.models import Recipe
import xmltodict


class BeerxmlParser:
    def parse(self, xml_content: str) -> Recipe:
        test = xmltodict.parse(xml_content, force_list={"YEAST", "HOP", "FERMENTABLE", "MISC", "WATER", "MASH_STEP"})
        return Recipe(**test["RECIPES"]["RECIPE"])
