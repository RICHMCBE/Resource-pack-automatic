import os
import json
import copy

json_text = '''
{
	"format_version": "1.10.0",
	"minecraft:attachable": {
		"description": {
			"identifier": "namespace:item_32",
			"render_controllers": ["controller.render.item_default"],
			"materials": {
				"default": "entity_alphatest",
				"enchanted": "entity_alphatest_glint"
			},
			"textures": {
				"default": "textures/entity/attachable/item_32",
				"enchanted": "textures/misc/enchanted_item_glint"
			},
			"geometry": {
				"default": "geometry.item_32"
			},
			"animations": {
				"first_person_hold": "animation.item_32.first_person_hold",
				"third_person_hold": "animation.item_32.third_person_hold"
			},
			"scripts": {
				"animate": [
					{
						"first_person_hold": "c.is_first_person"
					},
					{
						"third_person_hold": "!c.is_first_person"
					}
				]
			}
		}
	}
}
'''

# 문자열을 JSON(dict)로 변환
json_data = json.loads(json_text)

def get_png_files(directory):
    return [os.path.splitext(f)[0] for f in os.listdir(directory) if f.endswith('.png')]

def save_output(output_dir, final_data):

    for identifier in final_data:
        json_data_2 = copy.deepcopy(json_data)
        json_data_2["minecraft:attachable"]["description"]["identifier"] = f"cloud:{identifier}"
        json_data_2["minecraft:attachable"]["description"]["textures"]["default"] = f"textures/items/{identifier}"

        print(f"Identifier: {identifier}")

        os.makedirs(output_dir, exist_ok=True)  # 출력 디렉토리 생성
        output_file = os.path.join(output_dir, f"{identifier}.attachable.json")

        # json_string = json.dumps(json_data_2, indent=4, ensure_ascii=False)

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(json_data_2, file, indent=4, ensure_ascii=False)

        print(f"Output saved to {output_file}")
