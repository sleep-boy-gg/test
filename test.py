# from page_operation.basic import PageBasic
# a = PageBasic().get_screenshot("123")
# #
# import aircv as ac
# imgsrc = ac.imread(r'C:\Users\admin\Desktop\ui\user.png')   # xiaotu
# imgobj = ac.imread(r'C:\Users\admin\Documents\GitHub\xx\automated\test\screenshot\2024-04-17_11-33-13-123.png')
# match_result = ac.find_all_template(imgobj, imgsrc, 0.98)
# print('match_result:%s' % match_result)
# result_list = []
# if match_result is not None:
#     for data in match_result:
#         result_list.append(data['result'])
# else:
#     print('识别不到要点击的目标')
# print(result_list)

# match_result = ac.find_all_template(imgobj, imgsrc2, 0.95)
# print('match_result:%s' % match_result)
# result_list = []
# if match_result is not None:
#     for data in match_result:
#         result_list.append(data['result'])
# else:
#     print('识别不到要点击的目标')
# print(result_list)

# from common.feishu import FeiShu
#
# startTime = '2024-04-07 17:50:14'
# duration = '0:16:12.563423'
# total_count = 15
# success_count = 15
# failure_count = 0
# error_count = 0
# skip_count = 0
# result = "{}版本测试结果如下：测试开始时间为{}，持续时间为{}，共计用例{}条，成功{}条，失败{}条，异常{}条，跳过{}条".format(
#     '0.13.6',
#     startTime,
#     duration,
#     total_count,
#     success_count,
#     failure_count,
#     error_count,
#     skip_count)
# FeiShu().msg(result)
# print(result)

# import easyocr
# reader = easyocr.Reader(['en', 'ch_sim'], gpu=True)
# orc_result = reader.readtext(r'C:\Users\admin\Desktop\ui\ui_private_message_talk.png')
# print(orc_result)

# from common.ocr import ImgOcr
# print(ImgOcr('easyorc').get_string(r'C:\Users\admin\Desktop\ui\ui_private_message_talk.png'))

# ID: 030490

# import psutil
#
# # 获取所有进程及其启动时间
# processes = []
# for proc in psutil.process_iter(['pid', 'name', 'create_time']):
#     processes.append((proc.info['pid'], proc.info['name'], proc.info['create_time']))
#
# # 根据启动时间对进程进行排序
# sorted_processes = sorted(processes, key=lambda x: x[2])
#
# # 打印排序后的进程信息
# for pid, name, start_time in sorted_processes:
#     print(f"PID: {pid}, Name: {name}, Start Time: {start_time}")

# import yaml
# from pathlib import Path

# # 获取当前文件及当前项目的根目录所在的绝对路径
# current_path = Path(__file__).absolute()
# current_root_dir = current_path.parent.absolute()
#
#
# # 转换yaml文件的路径
# convert_yaml_path = current_root_dir.joinpath('page', 'convert.yaml')
# # 坐标地址yam文件的路径
# location_yaml_path = current_root_dir.joinpath('page', 'location.yaml')
#
# # 获取yaml文件中的数据
# with open(file=location_yaml_path, encoding='utf-8') as f:
#     location_yaml_data = yaml.safe_load(f)
#
# # 初始化待存储的yaml文件数据
# curr_location_yaml_data = location_yaml_data
# print(curr_location_yaml_data)
#
# # 默认仅写入最先识别到的文本信息
# curr_location_yaml_data['private_talk']['a']['b'] = [100, 200]
#
# with open(location_yaml_path, 'w') as f:
#     yaml.dump(curr_location_yaml_data, f)

# from common.ocr import ImgOcr
# print(ImgOcr.cmp_hash(r'C:\Users\admin\Desktop\ui\on.png', r'C:\Users\admin\Desktop\ui\on2.png'))
# print(ImgOcr.cmp_hash(r'C:\Users\admin\Desktop\ui\on.png', r'C:\Users\admin\Desktop\ui\off.png'))
# print(ImgOcr.cmp_hash(r'C:\Users\admin\Desktop\ui\on.png', r'C:\Users\admin\Desktop\ui\on.png'))

#
# from PIL import Image
#
# # 打开原始图片
# original_image = Image.open(r'C:\Users\admin\Desktop\ui\exp_no_search_result.png')  # 替换为你的图片路径
#
# # 定义原始图片和目标图片的尺寸
# original_width, original_height = original_image.size
# print(original_width, original_height)
# target_width, target_height = 290, 270
#
# # 计算截图的起始坐标（这里我们从顶部开始截取）
# left = 0  # 从左边开始
# top = (original_height - target_height) // 2  # 从中间位置开始截取，保证上下两侧均等截取
# right = target_width + left  # 右边坐标是目标宽度加上左边坐标
# bottom = target_height + top  # 底部坐标是目标高度加上顶部坐标
#
# # 截取图片
# cropped_image = original_image.crop((left, top, right, bottom))
#
# # 保存截取后的图片
# cropped_image.save(r'C:\Users\admin\Documents\GitHub\xx\automated\test\ui_png\exp_no_search_result.png')  # 保存为新的文件名

print("hello world")






