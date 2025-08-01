# -*- coding: utf-8 -*-
# crawl_detail 功能测试脚本

import asyncio
import os
import sys
from typing import Dict, Any, List

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import crawl_detail, set_config
import config
from tools import utils


class DetailTestRunner:
    """详情爬虫测试运行器"""
    
    def __init__(self):
        self.test_cases = [
            {
                "name": "小红书详情测试",
                "platform": "xhs",
                "store_type": "sqlite",
                "video_id": ["https://www.xiaohongshu.com/explore/64f2d2b9000000001300a8ec"]
            },
            {
                "name": "抖音详情测试", 
                "platform": "dy",
                "store_type": "sqlite",
                "video_id": ["7321219932050180387"]
            },
            {
                "name": "B站详情测试",
                "platform": "bili",
                "store_type": "sqlite", 
                "video_id": ["BV1d54y1g7db"]
            },
            {
                "name": "快手详情测试",
                "platform": "ks",
                "store_type": "sqlite",
                "video_id": ["3xf8enb8dbj6iae"]
            },
            {
                "name": "微博详情测试",
                "platform": "wb",
                "store_type": "sqlite",
                "video_id": ["4982041758140549"]
            }
        ]
        
    async def run_single_test(self, test_case: Dict[str, Any]) -> Dict[str, Any]:
        """运行单个测试用例"""
        print(f"\n🔍 开始测试: {test_case['name']}")
        print(f"  平台: {test_case['platform']}")
        print(f"  存储类型: {test_case['store_type']}")
        print(f"  视频ID: {test_case['video_id']}")
        
        start_time = asyncio.get_event_loop().time()
        
        try:
            # 设置测试环境变量
            self._set_test_env()
            
            result = await crawl_detail(
                platform=test_case['platform'],
                store_type=test_case['store_type'],
                video_id=test_case['video_id']
            )
            
            end_time = asyncio.get_event_loop().time()
            duration = end_time - start_time
            
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
        os.environ["CRAWLER_MAX_NOTES_COUNT"] = "3"  # 测试时减少爬取数量
        os.environ["MAX_CONCURRENCY_NUM"] = "2"      # 减少并发数
        os.environ["ENABLE_GET_COMMENTS"] = "True"   # 测试详情时获取评论
        
    async def run_all_tests(self) -> Dict[str, Any]:
        """运行所有测试用例"""
        print("🚀 开始 crawl_detail 功能测试\n")
        
        results = {}
        total_start_time = asyncio.get_event_loop().time()
        
        for i, test_case in enumerate(self.test_cases, 1):
            print(f"[{i}/{len(self.test_cases)}]", end=" ")
            test_result = await self.run_single_test(test_case)
            results[test_case['name']] = test_result
            
            # 测试间隔，避免请求过于频繁
            if i < len(self.test_cases):
                print("  ⏳ 等待5秒后进行下一个测试...")
                await asyncio.sleep(5)
        
        total_end_time = asyncio.get_event_loop().time()
        total_duration = total_end_time - total_start_time
        
        # 生成测试报告
        self._generate_report(results, total_duration)
        
        return results
    
    def _generate_report(self, results: Dict[str, Any], total_duration: float):
        """生成测试报告"""
        print("\n" + "="*60)
        print("📊 详情爬取测试报告")
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
    
    async def run_quick_test(self, platform: str = "bili", video_id: List[str] = ["BV1d54y1g7db"]):
        """快速测试单个平台"""
        print(f"🔍 快速测试 - 平台: {platform}, 视频ID: {video_id}")
        
        test_case = {
            "name": f"{platform}快速详情测试",
            "platform": platform,
            "store_type": "sqlite",
            "video_id": video_id
        }
        
        result = await self.run_single_test(test_case)
        return result


async def test_config_function():
    """测试配置设置功能"""
    print("🔧 测试详情配置设置功能...")
    
    # 测试详情配置
    test_video_ids = ["BV1d54y1g7db", "BV1Sz4y1U77N"]
    set_config(crawler_type="detail", platform="bili", video_id=test_video_ids)
    assert config.BILI_SPECIFIED_ID_LIST == test_video_ids
    print("  ✅ B站详情配置测试通过")
    
    # 测试小红书详情配置
    test_xhs_urls = ["https://www.xiaohongshu.com/explore/64f2d2b9000000001300a8ec"]
    set_config(crawler_type="detail", platform="xhs", video_id=test_xhs_urls)
    assert config.XHS_SPECIFIED_NOTE_URL_LIST == test_xhs_urls
    print("  ✅ 小红书详情配置测试通过")
    
    # 测试抖音详情配置
    test_dy_ids = ["7321219932050180387"]
    set_config(crawler_type="detail", platform="dy", video_id=test_dy_ids)
    assert config.DY_SPECIFIED_ID_LIST == test_dy_ids
    print("  ✅ 抖音详情配置测试通过")
    
    print("🎉 详情配置功能测试全部通过!")


async def test_multiple_ids():
    """测试多个ID同时爬取"""
    print("🔍 测试多个视频ID同时爬取...")
    
    # B站多个视频测试
    video_ids = ["BV1d54y1g7db", "BV1Sz4y1U77N"]
    
    try:
        result = await crawl_detail(
            platform="bili",
            store_type="sqlite",
            video_id=video_ids
        )
        
        if "success" in result.lower():
            print("✅ 多ID测试成功!")
            return True
        else:
            print(f"❌ 多ID测试失败: {result}")
            return False
            
    except Exception as e:
        print(f"💥 多ID测试异常: {str(e)}")
        return False


async def main():
    """主测试函数"""
    print("🚀 crawl_detail 测试套件\n")
    
    # 用户选择测试类型
    print("请选择测试类型:")
    print("1. 配置功能测试")
    print("2. 快速单平台测试")
    print("3. 多ID同时爬取测试")
    print("4. 完整功能测试")
    print("5. 自定义测试")
    
    try:
        choice = input("\n请输入选择 (1-5): ").strip()
        
        if choice == "1":
            await test_config_function()
            
        elif choice == "2":
            platform = input("请输入平台 (xhs/dy/bili/ks/wb): ").strip() or "bili"
            video_id_input = input("请输入视频ID/URL: ").strip() or "BV1d54y1g7db"
            video_ids = [video_id_input]
            
            runner = DetailTestRunner()
            await runner.run_quick_test(platform, video_ids)
            
        elif choice == "3":
            await test_multiple_ids()
            
        elif choice == "4":
            confirm = input("完整测试将运行所有平台，可能耗时较长，确认吗? (y/n): ").strip().lower()
            if confirm in ['y', 'yes']:
                runner = DetailTestRunner()
                await runner.run_all_tests()
            else:
                print("已取消测试")
                
        elif choice == "5":
            platform = input("请输入平台 (xhs/dy/bili/ks/wb/tieba/zhihu): ").strip()
            store_type = input("请输入存储类型 (sqlite/db/json/csv): ").strip() or "sqlite"
            video_id_input = input("请输入视频ID/URL (多个用逗号分隔): ").strip()
            
            if not platform or not video_id_input:
                print("❌ 平台和视频ID不能为空")
                return
                
            video_ids = [vid.strip() for vid in video_id_input.split(",")]
            
            print(f"\n开始自定义测试...")
            print(f"平台: {platform}")
            print(f"存储类型: {store_type}")
            print(f"视频ID: {video_ids}")
            
            # 设置测试环境
            os.environ["CRAWLER_MAX_NOTES_COUNT"] = "3"
            os.environ["MAX_CONCURRENCY_NUM"] = "2"
            os.environ["ENABLE_GET_COMMENTS"] = "True"
            
            result = await crawl_detail(platform, store_type, video_ids)
            print(f"测试结果: {result}")
            
        else:
            print("❌ 无效选择")
            
    except (EOFError, KeyboardInterrupt):
        print("\n🛑 测试被用户中断")
    except Exception as e:
        print(f"\n💥 测试过程中发生错误: {str(e)}")
        utils.logger.error(f"[detail_test] 测试失败: {str(e)}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 测试被用户中断")
    except Exception as e:
        print(f"\n💥 测试过程中发生未预期的错误: {str(e)}")
