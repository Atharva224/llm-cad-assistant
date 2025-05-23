import re

def prompt_to_openscad_code(prompt):
    prompt = prompt.lower()

    def get_val(pattern, default):
        match = re.search(pattern, prompt)
        return float(match.group(1)) if match else default

    if "hollow cylinder" in prompt:
        outer_d = get_val(r"outer diameter (\d+)", 20)
        thickness = get_val(r"thickness (\d+)", 2)
        height = get_val(r"height (\d+)", 50)
        outer_r = outer_d / 2
        inner_r = max(0.1, outer_r - thickness)

        return f"""difference() {{
    cylinder(h={height}, r={outer_r}, $fn=100);  // Outer
    cylinder(h={height}, r={inner_r}, $fn=100);  // Inner cut-out
}}"""
    

    elif "hollow cube" in prompt:
        side_match = re.search(r"hollow cube(?: of)? (\d+)", prompt)
        thickness_match = re.search(r"thickness (\d+)", prompt)

        if side_match:
            side = float(side_match.group(1))
        else:
            side = 40.0  # default

        if thickness_match:
            thickness = float(thickness_match.group(1))
        else:
            thickness = 2.0  # default

        # prevent invalid or zero thickness
        thickness = max(0.1, thickness)
        
        if 2 * thickness >= side:
            inner = 0.1
        else:
            inner = side - 2 * thickness

        return f"""difference() {{
        cube([{side}, {side}, {side}]);
        translate([{thickness}, {thickness}, {thickness}])
        cube([{inner}, {inner}, {inner}]);
}}"""



    elif "cube" in prompt:
        side = get_val(r"side (\d+)", 20)
        return f"cube([{side}, {side}, {side}]);"

    elif "sphere" in prompt:
        radius = get_val(r"radius (\d+)", 10)
        return f"sphere(r={radius}, $fn=100);"

    elif "stepped cylinder" in prompt:
        base_d = get_val(r"base diameter (\d+)", 30)
        top_d = get_val(r"top diameter (\d+)", 20)
        height = get_val(r"height (\d+)", 60)
        r1 = base_d / 2
        r2 = top_d / 2
        return f"""union() {{
    cylinder(h={height/2}, r={r1}, $fn=100);
    translate([0, 0, {height/2}])
    cylinder(h={height/2}, r={r2}, $fn=100);
}}"""

    

    elif "torus" in prompt:
        major = get_val(r"major radius (\d+)", 40)
        minor = get_val(r"minor radius (\d+)", 5)
        return f"""rotate_extrude($fn=100)
translate([{major}, 0, 0])
circle(r={minor}, $fn=50);"""

    elif "plate with" in prompt and "holes" in prompt:
        count = int(get_val(r"(\d+) holes", 4))
        rows = cols = int(count**0.5)
        spacing = get_val(r"spacing (\d+)", 30)
        plate_size = spacing * (rows + 1)
        hole_r = get_val(r"hole radius (\d+)", 3)
        plate_thickness = get_val(r"thickness (\d+)", 5)

        holes = "\n".join(
            f"    translate([{x * spacing}, {y * spacing}, 0]) cylinder(h={plate_thickness}, r={hole_r}, $fn=50);"
            for x in range(rows) for y in range(cols)
        )
        return f"""difference() {{
    cube([{plate_size}, {plate_size}, {plate_thickness}]);
{holes}
}}"""

    return "// Shape or parameters not recognized. Try: 'hollow cylinder with outer diameter 20mm and thickness 2mm'"
