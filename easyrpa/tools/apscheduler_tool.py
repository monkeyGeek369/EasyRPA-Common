from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.jobstores.memory import MemoryJobStore

class APSchedulerTool:
    _instance = None

    def __new__(cls, 
                 scheduler_type='background', 
                 executors=None, 
                 job_defaults=None, 
                 timezone='Asia/Shanghai', 
                 jobstores=None):
        if cls._instance is None:
            cls._instance = super(APSchedulerTool, cls).__new__(cls)
            cls._instance.scheduler = cls._instance._create_scheduler(scheduler_type=scheduler_type)
            cls._instance.scheduler.configure(
                executors=executors or cls._instance._default_executors(),
                job_defaults=job_defaults or cls._instance._default_job_defaults(),
                timezone=timezone,
                jobstores=jobstores or cls._instance._default_jobstores()
            )
        return cls._instance

    def _create_scheduler(self, scheduler_type):
        if scheduler_type == 'background':
            return BackgroundScheduler()
        # Add more scheduler types as needed
        raise ValueError(f'Unsupported scheduler type: {scheduler_type}')

    def _default_executors(self):
        return {
            'default': ThreadPoolExecutor(max_workers=10),
            'processpool': ProcessPoolExecutor(max_workers=5)
        }

    def _default_job_defaults(self):
        return {
            # 是否允许任务合并
            'coalesce': False,
            # 同时执行的最大任务数
            'max_instances': 3,
            # 表示任务错过执行的宽限时间（以秒为单位
            'misfire_grace_time': 30
        }

    def _default_jobstores(self):
        return {
            'default': MemoryJobStore()
        }

    def start(self):
        self.scheduler.start()

    def add_job(self, func, trigger, **kwargs):
        self.scheduler.add_job(func, trigger, **kwargs)

    def shutdown(self):
        self.scheduler.shutdown(wait=False)

    def get_all_jobs(self):
        return self.scheduler.get_jobs()
    
    def get_job(self, job_id):
        return self.scheduler.get_job(job_id)
    
    def delete_job(self, job_id):
        self.scheduler.remove_job(job_id)

    def __del__(self):
        self.shutdown()


if __name__ == '__main__':
    '''
    scheduler_tool = APSchedulerTool(
        scheduler_type='background',
        executors={
            'default': ThreadPoolExecutor(max_workers=10),
            'processpool': ProcessPoolExecutor(max_workers=5)
        },
        job_defaults={
            'coalesce': False,
            'max_instances': 3,
            'misfire_grace_time': 30
        },
        timezone='Asia/Shanghai',
        jobstores={
            'default': MemoryJobStore()
        }
    )

    # add test
    scheduler_tool.add_job(func=print,
                      trigger='cron',
                      second=1,
                      minute=1,
                      hour=1,
                      day=1,
                      month=1,
                      day_of_week=1,
                      kwargs={'job_id':123})
    scheduler_tool.add_job(func=print,
                      trigger='cron',
                      second=1,
                      minute=1,
                      hour=1,
                      day=1,
                      month=1,
                      day_of_week=1,
                      kwargs={'job_id':456})
    # get all jobs
    #all_jobs = scheduler_tool.get_all_jobs()
    # all_jobs[0].kwargs.get('job_id')
    # all_jobs[0].name
    #print(all_jobs)

    # get job by id
    #job = scheduler_tool.get_job(job_id="786381a7c0bb4a1ca9fbec4d75bdd79e")
    #print(job)

    # delete job
    #scheduler_tool.delete_job(job_id='e5ceb767e51044eea95026858452c73c')
    #print(scheduler_tool.get_all_jobs())
    '''