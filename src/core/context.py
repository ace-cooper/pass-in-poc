import contextvars
from typing import Dict, Any

main_context: contextvars.ContextVar[Dict[str, Any]] = contextvars.ContextVar('main_context', default={})

async def spawnNewCtx(ctx: Dict[str, Any], block, name='main') -> Any:
    namespace = contextvars.ContextVar(name, default={})
    return await withCtx(ctx, block, name, namespace)

async def withCtx(ctx: Dict[str, Any], block, name='main', cls=main_context) -> Any:
    local_ctx = ctx.copy()
    
    async def runner():
        data = cls.get()
        for key, value in local_ctx.items():
            if key == 'data':
                print('Cannot set data key in context')
                continue
            data[key] = value
        return await block(data)
    
    return await cls.run(runner)

def getCtx(name='main') -> Dict[str, Any]:
    return contextvars.ContextVar(name, default={}).get()

def get_ctx_data(name='main'):
    ctx = getCtx(name)
    
    def get(key):
        return ctx.get('data', {}).get(key)
    
    def set(key, value):
        if ctx:
            if 'data' not in ctx:
                ctx['data'] = {}
            ctx['data'][key] = value
    
    return {'get': get, 'set': set}