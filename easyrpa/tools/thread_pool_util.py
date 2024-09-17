import concurrent.futures
from easyrpa.tools import logs_tool

class ThreadPoolUtil:
    # 全局线程池字典
    global_thread_pools = {}

    @staticmethod
    def init_global_thread_pool(name, max_workers=5, thread_name_prefix='ThreadPool', initializer=None, initargs=()):
        """
        初始化全局线程池
        :param name: 全局线程池名称
        :param max_workers: 最大工作线程数
        :param thread_name_prefix: 线程名称前缀
        :param initializer: 线程初始化函数
        :param initargs: 线程初始化函数参数
        """
        try:
            ThreadPoolUtil.global_thread_pools[name] = concurrent.futures.ThreadPoolExecutor(
                max_workers=max_workers,
                thread_name_prefix=thread_name_prefix,
                initializer=initializer,
                initargs=initargs
            )
        except Exception as e:
            logs_tool.log_business_error("init_global_thread_pool","init global thread pool error",name,e)

    @staticmethod
    def get_global_thread_pool(name):
        """
        获取全局线程池
        :param name: 全局线程池名称
        :return: 全局线程池
        """
        return ThreadPoolUtil.global_thread_pools.get(name)

    @staticmethod
    def submit_task(name, task, *args, **kwargs):
        """
        提交任务到全局线程池
        :param name: 全局线程池名称
        :param task: 任务函数
        :param args: 任务函数参数
        :param kwargs: 任务函数关键字参数
        :return: 任务结果
        """
        try:
            global_thread_pool = ThreadPoolUtil.get_global_thread_pool(name)
            if global_thread_pool is None:
                raise Exception(f"global_thread_pool {name} not initialized")
            return global_thread_pool.submit(task, *args, **kwargs)
        except Exception as e:
            logs_tool.log_business_error("submit_task","submit task error",name,e)

    @staticmethod
    def map_tasks(name, tasks, *args, **kwargs):
        """
        并行执行多个任务
        :param name: 全局线程池名称
        :param tasks: 任务函数列表
        :param args: 任务函数参数
        :param kwargs: 任务函数关键字参数
        :return: 任务结果列表
        """
        try:
            global_thread_pool = ThreadPoolUtil.get_global_thread_pool(name)
            if global_thread_pool is None:
                raise Exception(f"global_thread_pool {name} not initialized")
            return list(global_thread_pool.map(lambda task: task(*args, **kwargs), tasks))
        except Exception as e:
            logs_tool.log_business_error("map_tasks","map tasks error",name,e)

    @staticmethod
    def shutdown_global_thread_pool(name):
        """
        关闭全局线程池
        :param name: 全局线程池名称
        """
        try:
            global_thread_pool = ThreadPoolUtil.get_global_thread_pool(name)
            if global_thread_pool is not None:
                global_thread_pool.shutdown()
        except Exception as e:
            logs_tool.log_business_error("shutdown_global_thread_pool","shutdown global thread pool error",name,e)

# 初始化全局线程池
#ThreadPoolUtil.init_global_thread_pool("pool1", max_workers=5, thread_name_prefix='MyThreadPool')

# 关闭全局线程池
#ThreadPoolUtil.shutdown_global_thread_pool("pool1")