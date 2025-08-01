# -*- coding: utf-8 -*-
# crawl_creator 功能测试脚本

import asyncio
import os
import sys
from typing import Dict, Any, List

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import crawl_creator, set_config
import config
import db
from tools import utils


class CreatorTestRunner:
    """创作者爬虫测试运行器"""
    
    def __init__(self):
        self.test_cases = [
            {
                "name": "小红书创作者测试",
                "platform": "xhs",
                "store_type": "sqlite",
                "creator_ids": ["5ff0e6410000000001001d33"]  # 示例创作者ID
            },
            {
                "name": "抖音创作者测试",
                "platform": "dy", 
                "store_type": "sqlite",
                "creator_ids": ["MS4wLjABAAAA5R2Q5q2gYzlmNzJ8VzQ"]  # 示例创作者ID
            },
            {
                "name": "B站UP主测试",
                "platform": "bili",
                "store_type": "sqlite",
                "creator_ids": ["477317922"]  # 示例UP主ID
            },
            {
                "name": "快手创作者测试",
                "platform": "ks",
                "store_type": "sqlite", 
                "creator_ids": ["3x9bq7t67p8shpw"]  # 示例创作者ID
            },
            {
                "name": "微博博主测试",
                "platform": "wb",
                "store_type": "sqlite",
                "creator_ids": ["1669879400"]  # 示例博主ID
            }
        ]
        
    async def run_single_test(self, test_case: Dict[str, Any]) -> Dict[str, Any]:
        """运行单个测试用例"""
        print(f"\n🔍 开始测试: {test_case['name']}")
        print(f"  平台: {test_case['platform']}")
        print(f"  存储类型: {test_case['store_type']}")
        print(f"  创作者ID: {test_case['creator_ids']}")
        
        start_time = asyncio.get_event_loop().time()
        
        try:
            # 设置测试环境变量
            self._set_test_env()
            
            result = await crawl_creator(
                platform=test_case['platform'],
                store_type=test_case['store_type'],
                creator_id=test_case['creator_ids']
            )
            
            end_time = asyncio.get_event_loop().time()
            duration = end_time - start_time
            
            # 确保数据库连接正确关闭
            try:
                await db.close()
            except Exception as close_e:
                print(f"  ⚠️ 关闭数据库连接时出现警告: {close_e}")
            
            if "success" in result.lower():
                print(f"  ✅ 测试成功! 耗时: {duration:.2f}秒")
                return {
                    "status": "success",
                    "duration": duration,
                    "result": result,
                    "error": None
                }
            else:
                print(f"  ❌ 测试失败: {result}")
                return {
                    "status": "failed",
                    "duration": duration,
                    "result": result,
                    "error": result
                }
                
        except Exception as e:
            # 确保即使出错也要关闭连接
            try:
                await db.close()
            except:
                pass
                
            end_time = asyncio.get_event_loop().time()
            duration = end_time - start_time
            error_msg = str(e)
            print(f"  💥 测试异常: {error_msg}")
            return {
                "status": "error",
                "duration": duration,
                "result": None,
                "error": error_msg
            }
    
    def _set_test_env(self):
        """设置测试环境变量"""
        os.environ["CRAWLER_MAX_NOTES_COUNT"] = "3"  # 减少爬取数量
        os.environ["MAX_CONCURRENCY_NUM"] = "1"      # 减少并发数
        os.environ["ENABLE_GET_COMMENTS"] = "False"  # 测试时不获取评论
        
    async def run_all_tests(self) -> Dict[str, Any]:
        """运行所有测试用例"""
        print("🚀 开始 crawl_creator 功能测试\n")
        
        results = {}
        total_start_time = asyncio.get_event_loop().time()
        
        for i, test_case in enumerate(self.test_cases, 1):
            print(f"[{i}/{len(self.test_cases)}]", end=" ")
            test_result = await self.run_single_test(test_case)
            results[test_case['name']] = test_result
            
            # 测试间隔，避免请求过于频繁，并确保资源清理
            if i < len(self.test_cases):
                print("  ⏳ 等待5秒后进行下一个测试...")
                await asyncio.sleep(5)
                
                # 强制垃圾回收
                import gc
                gc.collect()
        
        total_end_time = asyncio.get_event_loop().time()
        total_duration = total_end_time - total_start_time
        
        # 生成测试报告
        self._generate_report(results, total_duration)
        
        return results
    
    def _generate_report(self, results: Dict[str, Any], total_duration: float):
        """生成测试报告"""
        print("\n" + "="*60)
        print("📊 创作者爬虫测试报告")
        print("="*60)
        
        success_count = 0
        failed_count = 0
        error_count = 0
        
        for test_name, result in results.items():
            status_icon = {
                "success": "✅",
                "failed": "❌",
                "error": "💥"
            }.get(result["status"], "❓")
            
            print(f"{status_icon} {test_name}")
            print(f"    状态: {result['status']}")
            print(f"    耗时: {result['duration']:.2f}秒")
            
            if result.get('error'):
                print(f"    错误: {result['error']}")
            
            if result["status"] == "success":
                success_count += 1
            elif result["status"] == "failed":
                failed_count += 1
            else:
                error_count += 1
            print()
        
        print("-" * 60)
        print(f"总测试数: {len(results)}")
        print(f"成功: {success_count}")
        print(f"失败: {failed_count}")
        print(f"异常: {error_count}")
        print(f"总耗时: {total_duration:.2f}秒")
        print(f"成功率: {(success_count/len(results)*100):.1f}%")
        print("="*60)
    
    async def run_quick_test(self, platform: str = "bili", creator_ids: List[str] = ["477317922"]):
        """快速测试单个平台"""
        print(f"🔍 快速测试 - 平台: {platform}, 创作者ID: {creator_ids}")
        
        test_case = {
            "name": f"{platform}创作者快速测试",
            "platform": platform,
            "store_type": "sqlite",
            "creator_ids": creator_ids
        }
        
        result = await self.run_single_test(test_case)
        return result


async def test_config_function():
    """测试创作者配置设置功能"""
    print("🔧 测试创作者配置设置功能...")
    
    try:
        # 测试小红书创作者配置
        test_xhs_ids = ["5ff0e6410000000001001d33", "5ff0e6410000000001001d34"]
        set_config(crawler_type="creator", platform="xhs", creator_id=test_xhs_ids)
        assert config.XHS_CREATOR_ID_LIST == test_xhs_ids
        print("  ✅ 小红书创作者配置测试通过")
        
        # 测试抖音创作者配置
        test_dy_ids = ["MS4wLjABAAAA5R2Q5q2gYzlmNzJ8VzQ"]
        set_config(crawler_type="creator", platform="dy", creator_id=test_dy_ids)
        assert config.DY_CREATOR_ID_LIST == test_dy_ids
        print("  ✅ 抖音创作者配置测试通过")
        
        # 测试B站UP主配置
        test_bili_ids = ["477317922", "123456789"]
        set_config(crawler_type="creator", platform="bili", creator_id=test_bili_ids)
        assert config.BILI_CREATOR_ID_LIST == test_bili_ids
        print("  ✅ B站UP主配置测试通过")
        
        # 测试快手创作者配置
        test_ks_ids = ["3x9bq7t67p8shpw"]
        set_config(crawler_type="creator", platform="ks", creator_id=test_ks_ids)
        assert config.KS_CREATOR_ID_LIST == test_ks_ids
        print("  ✅ 快手创作者配置测试通过")
        
        # 测试微博博主配置
        test_wb_ids = ["1669879400"]
        set_config(crawler_type="creator", platform="wb", creator_id=test_wb_ids)
        assert config.WEIBO_CREATOR_ID_LIST == test_wb_ids
        print("  ✅ 微博博主配置测试通过")
        
        print("🎉 创作者配置功能测试全部通过!")
        
    except Exception as e:
        print(f"❌ 创作者配置测试失败: {str(e)}")


async def test_creator_id_validation():
    """测试创作者ID验证"""
    print("🔍 测试创作者ID格式验证...")
    
    test_cases = [
        {
            "platform": "xhs",
            "valid_ids": ["5ff0e6410000000001001d33", "60f0e6410000000001001d44"],
            "invalid_ids": ["", "invalid_id", "123"]
        },
        {
            "platform": "dy",
            "valid_ids": ["MS4wLjABAAAA5R2Q5q2gYzlmNzJ8VzQ"],
            "invalid_ids": ["", "short", "wrong_format"]
        },
        {
            "platform": "bili",
            "valid_ids": ["477317922", "123456789"],
            "invalid_ids": ["", "abc", "not_a_number"]
        }
    ]
    
    for test_case in test_cases:
        platform = test_case["platform"]
        print(f"  📱 测试 {platform} 平台:")
        
        # 测试有效ID
        for valid_id in test_case["valid_ids"]:
            if _is_valid_creator_id(platform, valid_id):
                print(f"    ✅ 有效ID: {valid_id}")
            else:
                print(f"    ❌ 应该有效但验证失败: {valid_id}")
        
        # 测试无效ID
        for invalid_id in test_case["invalid_ids"]:
            if not _is_valid_creator_id(platform, invalid_id):
                print(f"    ✅ 正确识别无效ID: {invalid_id}")
            else:
                print(f"    ❌ 应该无效但验证通过: {invalid_id}")


def _is_valid_creator_id(platform: str, creator_id: str) -> bool:
    """验证创作者ID格式是否有效"""
    if not creator_id or not creator_id.strip():
        return False
    
    if platform == "xhs":
        # 小红书ID通常是24位字符串
        return len(creator_id) >= 20 and creator_id.isalnum()
    elif platform == "dy":
        # 抖音ID通常以MS4wLjABAAAA开头
        return len(creator_id) >= 15
    elif platform == "bili":
        # B站UP主ID通常是数字
        return creator_id.isdigit() and len(creator_id) >= 6
    elif platform == "ks":
        # 快手ID格式相对灵活
        return len(creator_id) >= 8
    elif platform == "wb":
        # 微博博主ID通常是数字
        return creator_id.isdigit() and len(creator_id) >= 8
    
    return True  # 默认认为有效

async def main():
    """主测试函数"""
    print("🚀 crawl_creator 测试套件\n")
    
    # 用户选择测试类型
    print("请选择测试类型:")
    print("1. 创作者配置功能测试")
    print("2. 创作者ID验证测试")
    print("3. 快速单平台测试")
    print("4. 完整功能测试")
    print("5. 自定义测试")
    
    try:
        choice = input("\n请输入选择 (1-5): ").strip()
        
        if choice == "1":
            await test_config_function()
            
        elif choice == "2":
            await test_creator_id_validation()
            
        elif choice == "3":
            platform = input("请输入平台 (xhs/dy/bili/ks/wb): ").strip() or "bili"
            creator_id = input("请输入创作者ID: ").strip() or "477317922"
            
            runner = CreatorTestRunner()
            await runner.run_quick_test(platform, [creator_id])
            
        elif choice == "4":
            confirm = input("完整测试将运行所有平台，可能耗时较长，确认吗? (y/n): ").strip().lower()
            if confirm in ['y', 'yes']:
                runner = CreatorTestRunner()
                await runner.run_all_tests()
            else:
                print("已取消测试")
                
        elif choice == "5":
            platform = input("请输入平台 (xhs/dy/bili/ks/wb/tieba/zhihu): ").strip()
            store_type = input("请输入存储类型 (sqlite/db/json/csv): ").strip() or "sqlite"
            creator_ids_input = input("请输入创作者ID（多个用逗号分隔）: ").strip()
            
            if not platform or not creator_ids_input:
                print("❌ 平台和创作者ID不能为空")
                return
            
            creator_ids = [id.strip() for id in creator_ids_input.split(',') if id.strip()]
            
            print(f"\n开始自定义测试...")
            
            # 设置测试环境
            os.environ["CRAWLER_MAX_NOTES_COUNT"] = "3"
            os.environ["MAX_CONCURRENCY_NUM"] = "1" 
            os.environ["ENABLE_GET_COMMENTS"] = "False"
            
            try:
                result = await crawl_creator(platform, store_type, creator_ids)
                print(f"测试结果: {result}")
            except Exception as e:
                print(f"❌ 测试过程中发生错误: {str(e)}")
                utils.logger.error(f"[creator_test] 测试失败: {str(e)}")
            
        else:
            print("❌ 无效选择")
            
    except (EOFError, KeyboardInterrupt):
        print("\n🛑 测试被用户中断")
    except Exception as e:
        print(f"\n💥 测试过程中发生错误: {str(e)}")
        utils.logger.error(f"[creator_test] 测试失败: {str(e)}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 测试被用户中断")
    except Exception as e:
        print(f"\n💥 测试过程中发生未预期的错误: {str(e)}")
