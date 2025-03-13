<?php
namespace {{namespace}}\{{module_name}}\Plugin;

use Magento\Cms\Model\Block;

class CmsBlockTitleUpdater
{
    public function afterSetName(Block $subject, $name)
    {
        /**
            Add some code here
        */
        return $name;
    }
}
