import csv

def convert_ip_to_txt(input_filename, output_filename, num_entries=100):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            csv_reader = csv.reader(infile)
            next(csv_reader)  # 跳过标题行
            with open(output_filename, 'w', encoding='utf-8') as outfile:
                for i, row in enumerate(csv_reader):
                    if i >= num_entries:
                        break
                    if len(row) >= 4:
                        ip, datacenter, region, city = row[:4]
                        outfile.write(f"{ip}#{region}-{city}\n")
        print(f"已生成 {output_filename} 文件，包含前 {num_entries} 个IP地址及其位置信息")
    except FileNotFoundError:
        print(f"错误：找不到输入文件 {input_filename}")
    except Exception as e:
        print(f"发生错误：{str(e)}")

if __name__ == "__main__":
    input_file = r"C:\Users\sinos\Desktop\amclubs-cfnat-amd64\ip.csv"  # 使用 r 前缀
    output_file = "ip_locations.txt"
    convert_ip_to_txt(input_file, output_file, 100)